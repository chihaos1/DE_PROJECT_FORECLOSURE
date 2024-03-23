import os
import psycopg2
from dotenv import load_dotenv

async def delete_current_records():
	load_dotenv()

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