USE bird_box;

INSERT INTO usuario (nome, email, cidade) VALUES ("andre", "decoejz", "sp"), ("manu", "manuemmail", "campinas"), ("david", "davide@mail.com", "sao jose");

INSERT INTO preferencia (email, nome) VALUES ("decoejz", "passaro1"), ("decoejz", "pas2"), ("manuemmail","passa3");

INSERT INTO preferencia (email, nome) VALUES ("manuemmail","pas2");

INSERT INTO post (titulo, email) VALUES ("Era uma @decoejz avez...", "manuemmail");

INSERT INTO usuario_viu (email,id,so,ip,browser) VALUES ("ayres@linkadinho.inspermon.br",1,"WINDOWS","192.168.1.1","Internet Explorer");

INSERT INTO usuario_viu (email,id,so,ip,browser) VALUES ("decoejz",1,"WINDOWS","192.168.1.1","Internet Explorer");

INSERT INTO usuario_viu (email,id,so,ip,browser) VALUES ("manuemmail",1,"WINDOWS","192.168.1.1","Internet Explorer");

INSERT INTO usuario_viu (email,id,so,ip,browser) VALUES ("decoejz",2,"WINDOWS","192.168.1.1","Internet Explorer");

INSERT INTO usuario_viu (email,id,so,ip,browser) VALUES ("manuemmail",2,"WINDOWS","192.168.1.1","Internet Explorer");