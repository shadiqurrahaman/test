import schedule
import generate_student as gs

# ckeck elasticsearch is runnin

elasticsearch = gs.check_elasticserch()

if not elasticsearch:
    print("Start your Elasticsearch container")

# check the index exit or not

search_index = gs.check_index()

if not search_index:
    # if not create a new index
    response = gs.create_index()
    if response:
        print("Index created successgully")
    else:
        print("!!!Something went worng!!!")

# create search Index schema
search_index_confirm = gs.check_index()

if search_index_confirm :
    response = gs.create_index_schema()
    if response:
        print("Schema Created successfully")
    else:
        print("!!!Something went worng!!!")

# insert student
def runjob():
    for i in range(10):
        gs.insert_studet()

check_schema = gs.check_schema()

if check_schema:
    runjob()
    schedule.every(5).minutes.do(runjob)
    while True:
        schedule.run_pending()
       

    

