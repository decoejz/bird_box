USE bird_box;

ALTER TABLE post
    ADD COLUMN (
        likes INT NOT NULL DEFAULT 0,
        deslikes INT NOT NULL DEFAULT 0
    );

ALTER TABLE usuario_viu
    ADD COLUMN(
        liked SET('curtiu','nao curtiu','indiferente') NOT NULL DEFAULT ('indiferente')
    );