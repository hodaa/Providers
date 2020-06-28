from ParserInterface import ParserInterface


class DataProviderY(ParserInterface):
    def parse(self, data):
        status = {100: "authorised", 200: "decline", 300: "refunded"}
        list_y = []
        for item in data['users']:
            list_y.append(
                {
                    "provider": self.__class__.__name__,
                    "currency": item['balance'],
                    "amount": item['currency'],
                    "email": item['email'],
                    "status": status[item['status']],
                    "date": item["created_at"],
                    "identification": item["id"]
                }
            )

        return list_y
