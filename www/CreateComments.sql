CREATE TABLE Comments (commentid int not null auto_increment, username varchar(30), articleid int, comment_text varchar(500), comment_time timestamp default current_timestamp on update current_timestamp);