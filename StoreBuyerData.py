

Step 8.2: Store Buyer Data

        Now, let's save new buyers in the database.

        For PostgreSQL

	import psycopg2
	
	from psycopg2 import sql

	DB_CONFIG = {
    
		"dbname": "solana_tracker",
    		
                "user": "your_username",
    
	        "password": "your_password",
    
	        "host": "localhost",
    
	        "port": "5432"
	}

	def save_buyer(wallet, balance):
   	
	 try:
        
		conn = psycopg2.connect(**DB_CONFIG)
        
		cursor = conn.cursor()
        
        	query = sql.SQL("INSERT INTO buyers (wallet_address, balance) VALUES (%s, %s) ON CONFLICT DO NOTHING")
        
		cursor.execute(query, (wallet, balance))
        
        	conn.commit()
        
		cursor.close()
        	
		conn.close()
    
	except Exception as e:
        
	  print(f"Database error: {e}")


	for buyer in eligible_buyers:
    
	   save_buyer(buyer[0], buyer[1])