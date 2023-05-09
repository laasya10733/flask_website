from sqlalchemy import create_engine, text

db_connection_string="mysql+pymysql://1e761o9xia2t6u321fd3:pscale_pw_ii2oS9DqoX4awiNmXH9jFsg3CZi0xK6k9lEES7Fxk7f@aws.connect.psdb.cloud/careers?charset=utf8mb4"
engine = create_engine(db_connection_string, connect_args={
        "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    })

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
  jobs = []
  for row in result.all():
    jobs.append(row._mapping)
  return jobs

