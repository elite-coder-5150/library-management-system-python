class AdminDao():
    db = {}
    
    def __init__(self,Dao):
        self.db = Dao
        self.db.table = "admin"
        
    def get_by_id(self, id):
        sql = """
            --begin-sql
            select * from @table where id='{}'
            --end-sql
        """
        q = self.db.query(sql.format(id))
        user = q.fetchone()
        return user

    def get_by_email(self, email):
        sql = """
            --begin-sql
                select * from @table where email='{}'
            --end-sql
        """
        q = self.db.query(sql.format(email))
        user = q.fetchone()
        return user