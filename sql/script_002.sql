USE bird_box;

DROP TRIGGER IF EXISTS add_passaro_from_tag;
DROP TRIGGER IF EXISTS add_passaro_from_preferencia;

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
END //