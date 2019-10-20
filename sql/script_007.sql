USE bird_box;

INSERT INTO usuario (nome, email, cidade) VALUES ("andre", "decoejz", "sp");
INSERT INTO usuario (nome, email, cidade) VALUES ("manu", "manuemmail", "campinas");
INSERT INTO usuario (nome, email, cidade) VALUES ("david", "davide@mail.com", "sao jose");
INSERT INTO usuario (nome, email, cidade) VALUES ("usuario1", "use1@mail.com", "rj");
INSERT INTO usuario (nome, email, cidade) VALUES ("usuario2", "use2@mail.com", "sp");
INSERT INTO usuario (nome, email, cidade) VALUES ("usuario3", "use3@mail.com", "campinas");
INSERT INTO usuario (nome, email, cidade) VALUES ("usuario4", "use4@mail.com", "rj");
INSERT INTO usuario (nome, email, cidade) VALUES ("usuario5", "use5@mail.com", "sao jose");
INSERT INTO usuario (nome, email, cidade) VALUES ("usuario6", "use6@mail.com", "sao jose");

INSERT INTO passaro (nome) VALUES ("canario"),("beija-flor"),("sabia");

INSERT INTO preferencia (email, nome) VALUES ("decoejz", "passaro1"), ("decoejz", "pas2"), ("use2@mail.com","beija flor"), ("manuemmail","passa3");
INSERT INTO preferencia (email, nome) VALUES ("manuemmail","pas2"),("use5@mail.com","sabia");

INSERT INTO post (titulo, texto,email, url) VALUES ("Historinha","Era uma @decoejz avez...","manuemmail","google.img/canario");
INSERT INTO post (titulo, texto,email, url) VALUES ("Tardis","Era uma @use3@mail.com um passaro chamado #beija-flor que gosta de voar.","use1@mail.com","linkedin.passaros.com");
INSERT INTO post (titulo, texto,email, url) VALUES ("Um pais da europa","Tirou o @decoejz na copa dos #sabia","use3@mail.com","facebook.copinha.org.br");

INSERT INTO usuario_viu (email,id,so,ip,browser) VALUES ("davide@mail.com",1,"WINDOWS","192.168.1.1","Chorme");
INSERT INTO usuario_viu (email,id,so,ip,browser) VALUES ("decoejz",2,"UBUNTU","1.2.3.4","Internet Explorer");
INSERT INTO usuario_viu (email,id,so,ip,browser,liked) VALUES ("manuemmail",2,"WINDOWS","18.18.18.18","Internet Explorer","curtiu");
INSERT INTO usuario_viu (email,id,so,ip,browser,liked) VALUES ("use6@mail.com",2,"MACOS","192.168.0.1","Firefox","curtiu");
INSERT INTO usuario_viu (email,id,so,ip,browser,liked) VALUES ("use1@mail.com",2,"WINDOWS","19.16.1.1","Internet Explorer","nao curtiu");
INSERT INTO usuario_viu (email,id,so,ip,browser,liked) VALUES ("use4@mail.com",1,"MACOS","19.0.1.1","Safari","nao curtiu");

INSERT INTO tag_passaro (nome, id) VALUES ("canario",1),("beija-flor",2),("pas2",2),("sabia",3);

INSERT INTO tag_usuario (email, id) VALUES ("decoejz",1),("use1@mail.com",2),("decoejz",3),("use2@mail.com",1);