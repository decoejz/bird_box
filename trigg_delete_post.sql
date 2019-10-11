USE bird_box;

DROP TRIGGER IF EXISTS delete_post;

DELIMITER //
CREATE TRIGGER delete_post
BEFORE UPDATE ON post
FOR EACH ROW
BEGIN
	IF(OLD.ativo = 1 AND NEW.ativo = 0) THEN
		UPDATE tag_passaro SET tag_passaro.ativo = 0 WHERE tag_passaro.id = NEW.id;
        UPDATE tag_usuario SET tag_usuario.ativo = 0 WHERE tag_usuario.id = NEW.id;
        UPDATE usuario_viu SET usuario_viu.ativo = 0 WHERE usuario_viu.id = NEW.id;
	END IF;
END//
DELIMITER ;
