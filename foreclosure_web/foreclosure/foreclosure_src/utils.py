import os
import psycopg2

async def delete_current_records():

	conn = psycopg2.connect(host = "foreclosure-db.cq6va2rd6fnp.us-east-1.rds.amazonaws.com",
												dbname = "foreclosure",
												user = "csheng",
												password = "Orientatio135!",
												port = "5432")

	cur = conn.cursor()

	cur.execute(
		f"""

		DELETE FROM foreclosure_realtorproperties

		""")

	cur.execute(
		f"""
		
		DELETE FROM foreclosure_equatorproperties

		""")

	conn.commit()
	conn.close()