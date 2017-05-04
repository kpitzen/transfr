'''Flow control module'''

from routegetter import routesparser

if __name__ == '__main__':
    ROUTE_GETTER = routesparser.RouteGetter(url='http://www.cyride.com/index.aspx'
                                            , payload={'page':1212})
    ROUTE_GETTER.export_route_data()
