USE bird_box;

DROP VIEW IF EXISTS pop_cidade;
CREATE VIEW pop_cidade AS
    SELECT mv.nome, mv.email, mv.cidade, MAX(mv.cnt_vius)
    FROM (
        SELECT usuario.nome, usuario.email, usuario.cidade, COUNT(usuario_viu.id) as cnt_vius 
        FROM usuario 
        INNER JOIN post USING (email)
        INNER JOIN usuario_viu USING (id)
        GROUP BY usuario_viu.id) AS mv
    GROUP BY mv.cidade
    ORDER BY mv.cidade;