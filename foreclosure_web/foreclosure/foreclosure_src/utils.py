import os
import psycopg2

async def delete_current_records():

	conn = psycopg2.connect(host = os.getenv("DB_HOST"),
													dbname = os.getenv("DB_NAME"),
													user = os.getenv("DB_USER"),
													password = os.getenv("DB_PASSWORD"),
													port = os.getenv("DB_PORT"))

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