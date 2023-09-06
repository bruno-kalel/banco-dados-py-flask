import psycopg2

with psycopg2.connect(database='',
                      user='',
                      password='',
                      host='',
                      port='') as conn:
    def resgatar_info(argumento):
        with conn.cursor() as cur:
            cur.execute(argumento)
            dados = str(print(cur.fetchall()))
            return dados

    def pesquisar_por_varchar(argumento):
        query = f"SELECT matricula FROM public.aluno WHERE (nome_inicio ||' '|| nome_resto) LIKE '%{argumento}%'"
        resgatar_info(query)
