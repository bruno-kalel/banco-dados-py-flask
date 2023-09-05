import psycopg2
pesquisar_por = 'bruno'

with psycopg2.connect(database='classroom_automation',
                      user='',
                      password='',
                      host='',
                      port='') as conn:
    def resgatar_info(argumento):
        with conn.cursor() as cur:
            cur.execute(argumento)
            print(cur.fetchall())
            return

    def pesquisar_por_varchar(argumento):
        query = f"SELECT matricula FROM public.aluno WHERE (nome_inicio ||' '|| nome_resto) LIKE '%{argumento}%'"
        resgatar_info(query)


pesquisar_por_varchar(pesquisar_por)
