def db_formatter(formatted):
    import os
    import mysql.connector
    from pathlib import Path
    from dotenv import load_dotenv
    import warnings

    env_path = Path('.', '.env')
    load_dotenv(dotenv_path=env_path)

    db_host = os.getenv('MYSQL_DATABASE_HOST')
    # print(db_host)
    db_user = os.getenv('MYSQL_DATABASE_USERNAME')
    # print(db_user)
    db_pass = os.getenv('MYSQL_DATABASE_PASSWORD')
    # print(db_pass)
    db_db = os.getenv('MYSQL_DATABASE_DATABASE')

    mydb = mysql.connector.connect(
        host=db_host,
        user=db_user,
        password=db_pass,
        database=db_db
    )

    mycursor = mydb.cursor()

    table_check1 = True
    table_check2 = True
    table_check3 = True
    table_check4 = True
    table_check5 = True

    # mycursor.execute("DROP TABLE bundle_session_id")

    mycursor.execute("CREATE TABLE IF NOT EXISTS auth_id (auth_id VARCHAR(255), origin_url VARCHAR(255), validate_id "
                     "VARCHAR(255))")
    warnings.filterwarnings("ignore")
    mycursor.execute("CREATE TABLE IF NOT EXISTS artsy_upload (bundle_id VARCHAR(255))")
    warnings.filterwarnings("ignore")
    mycursor.execute("CREATE TABLE IF NOT EXISTS accounts (id INT AUTO_INCREMENT PRIMARY KEY, email VARCHAR(255), "
                     "username VARCHAR( "
                     "255), "
                     "password VARCHAR( 255))")
    warnings.filterwarnings("ignore")
    mycursor.execute("CREATE TABLE IF NOT EXISTS bundle_profile (bundle_id INT AUTO_INCREMENT PRIMARY KEY, "
                     "artist_name_first VARCHAR( 255), artist_name_last VARCHAR(255), art_medium VARCHAR(255), "
                     "price VARCHAR(255), bundle_image_profile_id VARCHAR(255), art_dimensions VARCHAR(255), "
                     "artwork_name VARCHAR(255))")
    warnings.filterwarnings("ignore")
    mycursor.execute("CREATE TABLE IF NOT EXISTS bundle_image_profile (id INT AUTO_INCREMENT PRIMARY KEY, "
                     "image_1 VARCHAR(255), image_2 VARCHAR(255), image_3 VARCHAR(255), image_4 VARCHAR(255), "
                     "image_5 VARCHAR(255))")
    warnings.filterwarnings("ignore")

    if not (table_check1 or table_check2 or table_check3 or table_check4 or table_check5):
        print("Failed")
        return formatted == False
    else:
        print("Succeeded")
        return formatted == True
