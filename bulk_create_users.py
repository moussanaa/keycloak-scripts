from keycloak import KeycloakOpenID
from keycloak import KeycloakAdmin
import json

keycloak_admin = KeycloakAdmin(server_url="http://sso-server:8080/auth/",
                               username='admin-demo',
                               password='admin',
                               realm_name="demo-realm",
                               client_secret_key="",
                               verify=True)

with open('list_users.json') as json_file:
    data = json.load(json_file)
    for a_user in data['users']:
        new_user = keycloak_admin.create_user({
                    "email": a_user['email'],
                    "username": a_user['username'],
                    "enabled": a_user['enabled'],
                    "firstName": a_user['firstName'],
                    "lastName": a_user['lastName']})

keycloak_admin.keycloak_openid.logout
