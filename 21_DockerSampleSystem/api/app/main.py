import os
import logging
import pymysql
from fastapi import FastAPI, HTTPException

# ログ設定
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler_docker = logging.FileHandler("/proc/1/fd/1")
handler_docker.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
logger.addHandler(handler_docker)

app = FastAPI()
logger.info("REST API Server started")

@app.get("/version")
def get_version():
    logger.info("called /version")
    return {"version": "1.0.0"}

@app.get("/api/prefectures")
def get_prefectures():
    logger.info("called /api/prefectures")
    conn = None
    try:
        conn = pymysql.connect(
            host=os.environ["DB_HOST"],
            port=int(os.environ["DB_PORT"]),
            user=os.environ["DB_USER"],
            password=os.environ["DB_PASSWORD"],
            database=os.environ["DB_NAME"]
        )
        with conn.cursor() as cursor:
            cursor.execute("SELECT name FROM prefectures")
            results = cursor.fetchall()
        return {"prefectures": [row[0] for row in results]}

    except pymysql.MySQLError as e:
        logger.error(f"MySQL Error: {e}")
        raise HTTPException(status_code=500, detail="Database error occurred.")
    except KeyError as e:
        logger.error(f"Environment variable missing: {e}")
        raise HTTPException(status_code=500, detail="Server configuration error.")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="Unexpected server error.")
    finally:
        if conn and conn.open:
            try:
                conn.close()
            except Exception as e:
                logger.warning(f"Failed to close connection: {e}")