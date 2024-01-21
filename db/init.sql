create table movie_table(
	id SERIAL primary KEY,
	name VARCHAR(50),
	content VARCHAR(200),
	created_date TIMESTAMP default current_timestamp
);

insert into movie_table(name, content)
values
	('괴물', '긴장감 넘치네'),
	('나는 내일 어제의 너와 만난다', '두 번 볼 때 울어'),
	('아바타2', '아바타는 레알 전설이다');