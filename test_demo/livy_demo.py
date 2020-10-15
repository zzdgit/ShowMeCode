import json, pprint, requests, textwrap


data = {
  'code': textwrap.dedent("""
    import random
    NUM_SAMPLES = 100000
    def sample(p):
      x, y = random.random(), random.random()
      return 1 if x*x + y*y < 1 else 0

    count = sc.parallelize(xrange(0, NUM_SAMPLES)).map(sample).reduce(lambda a, b: a + b)
    print "Pi is roughly %f" % (4.0 * count / NUM_SAMPLES)
    """)
}


class LivySession:
    def __init__(self):
        self.host = 'http://10.202.80.138:8998'
        # self.host = 'http://10.202.41.81:8998'
        self.session_url = self.host + '/sessions'
        self.headers = {'Content-Type': 'application/json'}
        self.sess_conf = {"kind": "pyspark"}

    def create_session(self):
        r = requests.post(self.session_url, data=json.dumps(self.sess_conf), headers=self.headers)
        return r.json()

    def commit_task(self, data):
        sess = self.create_session()
        sess_id = sess.get('id')
        statements_url = self.session_url + '/' + str(sess_id) + '/statements'
        #statements_url = self.session_url + '/0/statements'
        r = requests.post(statements_url, data=json.dumps(data), headers=self.headers)
        return r.json()

    def delete_session(self):
        r = requests.delete(self.session_url, headers=self.headers)
        print(r.json())

    def logs_session(self):
        log_url = self.session_url + '/logs'
        r = requests.get(log_url, headers=self.headers)
        print(r.json)


# url = 'http://10.202.80.138:8998/sessions'
# r = requests.get(url)
# # print(r.json())

ls = LivySession()
r = ls.commit_task(data)
print(r)

# headers = {'Content-Type': 'application/json'}
# statements_url = 'http://10.202.80.138:8998/sessions/1/statements'
# r = requests.post(statements_url, data=json.dumps(data), headers=headers)
# print(r.json())

# statement_url = host + '/sessions/0/statements/0'
# r = requests.get(statement_url, headers=headers)
# pprint.pprint(r.json())
# pprint.pprint(r.headers)

# session_url = 'http://localhost:8998/sessions/0'
# r = requests.delete(session_url, headers=headers)
# print(r.json())

# log_url = session_url + '/logs'
# r = requests.get(log_url, headers=headers)
# print(r.json)

