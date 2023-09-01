import xmlrpc.client

url = "http://localhost:8082"
db = "odoo_test"
username = "saira.tabassum@bedatasolutions.com"
password = "121998"

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
# print('version info',common.version())

# authentication
uid = common.authenticate(db, username, password, {})
print('UID', uid)

if uid:
    # print("authentication success", uid)
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

    # search method
    # partners_ids = models.execute_kw(db, uid, password, 'res.partner', 'search',
    #                                  [[['is_company', '=', True]]])
    # print(partners_ids)

    # search count
    # partners_count = models.execute_kw(db, uid, password, 'res.partner', 'search_count',
    #                                    [[['is_company', '=', True]]])
    # print(partners_count)

    # read method
    # partner_rec = models.execute_kw(db, uid, password, 'res.partner', 'read', [partners_ids],
    #                                 {'fields': ['id', 'name']})
    # for rec in partner_rec:
    #     print(rec)

    # search and read
    # partners_rec2 = models.execute_kw(db, uid, password, 'res.partner', 'search_read', [[['is_company', '=', True]]],
    #                                   {'fields': ['name', 'country_id', 'comment'], 'limit': 2})
    # print(partners_rec2)

    # create
    # vals = {
    #     "name": "Odoo Mates External API",
    #     "email": "odoomates@gmail.com"
    # }
    # created_id = models.execute_kw(db, uid, password, 'res.partner', 'create', [vals])
    # print("created record->", created_id)

    # update
    search_email = models.execute_kw(db, uid, password, 'res.partner', 'search',
                                     [[['email', '=', 'demo@gmail.com']]])

    models.execute_kw(db, uid, password, 'res.partner', 'write', [search_email, {'phone': "009", "mobile": "001"}])

    # delete
    email = models.execute_kw(db, uid, password, 'res.partner', 'search',
                              [[['email', '=', 'test@gmail.com']]])

    models.execute_kw(db, uid, password, 'res.partner', 'unlink', [email])



else:
    print("authentication failed")
