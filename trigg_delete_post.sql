USE bird_box;

DROP TRIGGER IF EXISTS delete_post;

DELIMITER //
CREATE TRIGGER delete_post
BEFORE UPDATE ON post
FOR EACH ROW
BEGIN
	IF(OLD.ativo = 1 AND OLD.ativo = 0) THEN
		DELETE FROM tag_passaro WHERE tag_passaro.id = post.id;
        DELETE FROM tag_usuario WHERE tag_usuario.id = post.id;
        UPDATE usuario_viu SET usuario_viu.ativo = 0 WHERE usuario_viu.id = post.id;
	END IF;
END//
DELIMITER ;
