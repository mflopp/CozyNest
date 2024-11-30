# Logic for working with business processes

user_test_data.py adds test users directly to the DB using hardcode

Have 2 functions inside:
1. add_test_users - Must be used only once at the empty DB
2. add_test_users_check_if - Can be used any time, it will add only missing test users
