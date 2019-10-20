USE bird_box;

ALTER TABLE post
    ADD COLUMN (
        data_post TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    );

ALTER TABLE usuario_viu
    ADD COLUMN(
        liked SET('curtiu','nao curtiu','indiferente') NOT NULL DEFAULT ('indiferente')
    );