from flask import Flask, request, jsonify

from custom_exceptions.custom_exception_message import CustomExceptionMessage
from data_access_layer.implementation_classes.account_postgres_dao import AccountPostgresDao
from data_access_layer.implementation_classes.user_postgres_dao import UserPostgresDao
from entities.accounts import Account
from entities.users import User
from service_layer.implementation_services.account_service_imp import AccountServiceImp
from service_layer.implementation_services.user_service_imp import UserServiceImp
import logging
from flask_cors import CORS

logging.basicConfig(filename='records.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(message)s')

STATIC_FOLDER = 'templates/assets'
app = Flask(__name__, static_folder=STATIC_FOLDER)
CORS(app)
account_dao = AccountPostgresDao()
user_dao = UserPostgresDao()
user_service = UserServiceImp(user_dao, account_dao)
account_service = AccountServiceImp(account_dao, user_dao)


@app.route('/')
def index():
    return "Landing page"


@app.errorhandler(404)
def invalid_route():
    return "Nice try!! Invalid route"


@app.errorhandler(500)
def internal_error():
    return "I messed up somewhere. "


@app.post("/account/create")
def create_account_entry():
    try:
        account_data = request.get_json()
        new_account = Account(
            int(account_data["accountId"]),
            str(account_data["accountName"]),
            int(account_data["userId"]),
            float(account_data["balance"]))
        account_to_return = account_service.service_create_account_entry(new_account)
        account_as_dictionary = account_to_return.make_account_dictionary()
        account_as_json = jsonify(account_as_dictionary)
        return account_as_json
    except CustomExceptionMessage as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json
    except ValueError as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json
    except KeyError as e:
        exception_dictionary = {"message": "Please change JSON keys to " + str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json


@app.get('/account/<account_id>')
def get_account_information(account_id):
    try:
        account_information = account_service.service_get_account_information(int(account_id))
        account_information_dict = {
            'accountName': account_information.account_name,
            'userId': account_information.user_id,
            'accountId': account_information.account_id,
            'balance': account_information.balance,
        }
        return jsonify(account_information_dict)
    except CustomExceptionMessage as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json
    except ValueError as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json


@app.get('/account/all')
def get_all_account_information():
    accounts_list = account_service.service_get_all_accounts_information()
    account_dict = []
    for a in accounts_list:
        account_dict.append(a.make_account_dictionary())
    return jsonify(account_dict)


@app.patch('/account/update')
def update_account_information():
    try:
        updated_account = request.get_json()
        updated_account_obj = Account(
            int(updated_account["accountId"]),
            str(updated_account["accountName"]),
            int(updated_account["userId"]),
            float(updated_account["balance"])
        )
        account_to_update = account_service.service_update_account_information(updated_account_obj)
        updated_account_as_dict = account_to_update.make_account_dictionary()
        return jsonify(updated_account_as_dict)
    except CustomExceptionMessage as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json
    except ValueError as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json
    except KeyError as e:
        exception_dictionary = {"message": "Please change JSON keys to " + str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json


@app.patch('/account/deposit')
def deposit_fund_account():
    try:
        deposit_data = request.get_json()
        returned_account = account_service.service_deposit_funds(
            int(deposit_data["accountId"]),
            float(deposit_data['amount'])
        )
        returned_account_as_dic = returned_account.make_account_dictionary()
        return jsonify(returned_account_as_dic)
    except CustomExceptionMessage as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json
    except ValueError as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json
    except KeyError as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json


@app.patch('/account/withdraw')
def withdraw_fund_account():
    try:
        deposit_data = request.get_json()
        returned_account = account_service.service_withdraw_funds(
            int(deposit_data["accountId"]),
            float(deposit_data['amount'])
        )
        returned_account_as_dic = returned_account.make_account_dictionary()
        return jsonify(returned_account_as_dic)
    except CustomExceptionMessage as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json
    except ValueError as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json
    except KeyError as e:
        exception_dictionary = {"message": "Please change JSON keys to " + str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json


@app.patch('/account/transfer')
def transfer_fund_account():
    try:
        transfer_data = request.get_json()
        accounts_to_return = account_service.service_transfer_fund_account(
            int(transfer_data["accountId"]),
            int(transfer_data['accountToTransferId']),
            float(transfer_data['amount'])
        )
        updated_accounts = {}
        for a in accounts_to_return:
            updated_accounts[a.account_id] = a.make_account_dictionary()
        return jsonify(updated_accounts)
    except CustomExceptionMessage as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json
    except ValueError as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json
    except KeyError as e:
        exception_dictionary = {"message": "Please change JSON keys to " + str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json


@app.delete('/account/delete/<account_id>')
def delete_account_information(account_id):
    try:
        account_information = account_service.service_get_account_information(int(account_id))
        account_information_dict = {
            'Deleted': 'Account',
            'accountName': account_information.account_name,
            'userId': account_information.user_id,
            'accountId': account_information.account_id,
            'balance': account_information.balance,
        }
        account_service.service_delete_account_information(int(account_id))
        return jsonify(account_information_dict)
    except CustomExceptionMessage as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json
    except ValueError as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json


# =================================================================================

@app.post("/user/create")
def create_user_entry():
    try:
        user_data = request.get_json()
        new_user = User(
            int(user_data["userId"]),
            str(user_data["firstName"]),
            str(user_data["lastName"])
        )
        user_to_return = user_service.service_create_user_entry(new_user)
        user_as_dictionary = user_to_return.make_user_dictionary()
        user_as_json = jsonify(user_as_dictionary)
        return user_as_json
    except ValueError as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json
    except KeyError as e:
        exception_dictionary = {"message": "Please change JSON keys to " + str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json


@app.get('/user/<user_id>')
def get_user_information(user_id):
    try:
        user_data = user_service.service_get_user_information(int(user_id))
        user_information_dict = {
            "userId": user_data.user_id,
            "firstName": user_data.first_name,
            "lastName": user_data.last_name
        }
        return jsonify(user_information_dict)
    except CustomExceptionMessage as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json
    except ValueError as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json


@app.get('/user/all')
def get_all_user_information():
    users_list = user_service.service_get_all_users_information()
    user_dict = {}
    for a in users_list:
        user_dict[a.user_id] = a.make_user_dictionary()
    return jsonify(user_dict)


@app.patch('/user/update')
def update_user_information():
    try:
        updated_user = request.get_json()
        updated_user_obj = User(
            int(updated_user["userId"]),
            str(updated_user["firstName"]),
            str(updated_user["lastName"])
        )
        user_to_update = user_service.service_update_user_information(updated_user_obj)
        updated_user_as_dict = user_to_update.make_user_dictionary()
        return jsonify(updated_user_as_dict)
    except CustomExceptionMessage as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json
    except ValueError as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json
    except KeyError as e:
        exception_dictionary = {"message": "Please change JSON keys to " + str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json


@app.delete('/user/delete/<user_id>')
def delete_user_information(user_id):
    try:
        user_data = user_service.service_get_user_information(int(user_id))
        user_information_dict = {
            'Deleted': 'User',
            'userId': user_data.user_id,
            'firstName': user_data.first_name,
            'lastName': user_data.last_name
        }
        user_service.service_delete_user_information(int(user_id))
        return jsonify(user_information_dict)
    except CustomExceptionMessage as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json
    except ValueError as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json


app.run()
