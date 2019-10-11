USE bird_box;
DROP PROCEDURE IF EXISTS add_tag_usuario;

DELIMITER //
CREATE PROCEDURE add_tag_usuario(IN var_email VARCHAR(40), IN var_id INT)
BEGIN
	IF (SELECT IF((SELECT COUNT(email) FROM usuario WHERE email=var_email)>0, 1,0) = 1) THEN
		INSERT INTO tag_usuario (email, id) VALUES (var_email, var_id);
    END IF;
END//
DELIMITER ;