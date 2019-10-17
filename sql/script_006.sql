USE bird_box;

DROP TEMPORARY TABLE IF EXISTS max_vius_cid;
CREATE TEMPORARY TABLE max_vius_cid
	SELECT usuario.nome, usuario.email, usuario.cidade, COUNT(usuario_viu.id) as cnt_vius 
		FROM usuario 
		INNER JOIN post USING (email)
		INNER JOIN usuario_viu USING (id)
		GROUP BY usuario.cidade;

DROP VIEW pop_cidade AS
    SELECT mv.nome, mv.email, mv.cidade, MAX(mv.cnt_vius)
    FROM max_vius_cid mv
    GROUP BY mv.cidade
    ORDER BY mv.cidade;