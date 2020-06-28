from ParserInterface import ParserInterface


class DataProviderX(ParserInterface):
    def parse(self, data):
        status = {1: "authorised", 2: "decline", 3: "refunded"}
        list_x = []
        for item in data['users']:
            list_x.append({
                "provider": self.__class__.__name__,
                "currency": item['Currency'],
                "amount": item['parentAmount'],
                "email": item['parentEmail'],
                "status": status[item['statusCode']],
                "date": item["registerationDate"],
                "identification": item["parentIdentification"]
            }
            )

        return list_x
