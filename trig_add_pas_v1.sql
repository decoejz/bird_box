USE bird_box;

DROP TRIGGER IF EXISTS add_passaro_from_tag;
DROP TRIGGER IF EXISTS add_passaro_from_preferencia;
DROP PROCEDURE IF EXISTS add_tag_usuario;

DELIMITER //
CREATE TRIGGER add_passaro_from_tag
BEFORE INSERT ON tag_passaro
FOR EACH ROW
BEGIN
	IF NOT(NEW.nome IN (SELECT * FROM passaro)) THEN
		INSERT INTO passaro (nome) VALUES (NEW.nome);
	END IF;
END;

CREATE TRIGGER add_passaro_from_preferencia
BEFORE INSERT ON preferencia
FOR EACH ROW
BEGIN
	IF NOT(NEW.nome IN (SELECT * FROM passaro)) THEN
		INSERT INTO passaro (nome) VALUES (NEW.nome);
	END IF;
END;

CREATE PROCEDURE add_tag_usuario(IN email VARCHAR(40), id INT)
BEGIN
    IF (email IN (SELECT email FROM usuario)) THEN
		INSERT INTO tag_usuario (email, id) VALUES (email, id);
	END IF;
END//