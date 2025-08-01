import json

class DB(object):
    __data = {}
    def __init__(self, db):
        if db is not None:
            self.__data = db
        else:
            self.__data = {"users": []}

    def get_users(self, users = None):
        """ Method to get users conditionally """
        if users is None:
            return self.__data
        out = []
        for user in self.__data['users']:
            if user['name'] in users:
                out.append(user)
        return {"users": out}

    def add_user(self, user):
        user_obj = {
            "name": user,
            "owes": {},
            "owed_by": {},
            "balance": 0
        }
        self.__data['users'].append(user_obj)
        return user_obj
    
    def delend(self, name, other):
        """
            If user, both owes and is owed by the same person, clean that record.
        """
        x = 0 
        while x < len(self.__data["users"]):
            user = self.__data["users"][x]

            if name == user['name']:
                if other in user['owes'].keys() and other in user['owed_by'].keys():
                    if user['owes'][other] > user['owed_by'][other]:
                        user['owes'][other] -= user['owed_by'][other]
                        if user['owes'][other] == 0:
                            del user['owes'][other]
                        del user['owed_by'][other]
                    else:
                        user['owed_by'][other] -= user['owes'][other]
                        if user['owed_by'][other] == 0:
                            del user['owed_by'][other]
                        del user['owes'][other]

                else:
                    return


            x += 1

    def add_iou(self, lender, borrower, amount):
        x = 0 
        while x < len(self.__data["users"]):
            user = self.__data["users"][x]
            if user['name'] == lender:
                if borrower in user["owed_by"].keys():
                    user["owed_by"][borrower] += float(amount)
                else:
                    user["owed_by"][borrower] = float(amount)
                
                user['balance'] = sum(user['owed_by'].values()) - sum(user['owes'].values())

            if user['name'] == borrower:
                if borrower in user["owes"].keys():
                    user["owes"][lender] += float(amount)
                else:
                    user["owes"][lender] = float(amount)

                user['balance'] = sum(user['owed_by'].values()) - sum(user['owes'].values())
            
            x += 1
        
        self.delend(lender, borrower)
        self.delend(borrower, lender)
            


class RestAPI(object):
    def __init__(self, database=None):
        self.database = DB(database)

    def get(self, url, payload=None):
        if payload:
            payload = json.loads(payload)
        else:
            payload = {"users": []}
        

        if url == '/users':
            return json.dumps(self.database.get_users(payload["users"]))

    def post(self, url, payload=None):
        if not payload:
            return "500"
        payload = json.loads(payload)
        if url == "/add":
            return json.dumps(self.database.add_user(payload['user']))
        if url == "/iou":
            self.database.add_iou(payload['lender'], payload['borrower'], payload['amount'])
            return self.get("/users", json.dumps({'users': [payload['lender'], payload['borrower']]}) )

