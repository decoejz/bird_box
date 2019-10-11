DROP PROCEDURE IF EXISTS add_tag_usuario;

DELIMITER //
CREATE PROCEDURE add_tag_usuario(IN email VARCHAR(40), IN id INT)
BEGIN
    IF (email IN (SELECT * FROM usuario)) THEN
		INSERT INTO tag_usuario (email, id) VALUES (email, id);
	END IF;
END//
DELIMITER ;