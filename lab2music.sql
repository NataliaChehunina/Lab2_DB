create database `lab2music`;
use `lab2music`;

create table `artists` (
	`id` int(10) not null auto_increment,
	`name` varchar(100) not null,
	`country` varchar(100) not null,
	primary key (`id`)
);

create table `studios` (
	`id` int(10) not null auto_increment,
	`name` varchar(100) not null,
	primary key (`id`)
);

create table `albums` (
	`id` int(10) not null auto_increment,
	`name` varchar(100) not null,
	`year` int(4) not null,
	`artist_id` int(10) not null,
	`style` varchar(100) not null,
	`studio_id` int(10) not null,
	primary key (`id`),
	foreign key (`artist_id`) references `artists`(`id`) on delete cascade,
	foreign key (`studio_id`) references `studios`(`id`) on delete cascade
);

create table `tracks` (
	`id` int(10) not null auto_increment,
	`name` varchar(100) not null,
	`duration` varchar(100) not null,
	`date_record` varchar(100) not null,
	`album_id` int(10) not null,
	primary key (`id`),
	foreign key (`album_id`) references `albums`(`id`) on delete cascade
);

-- alter table `tracks` add constraint `tracks_fk0` foreign key (`album_id`) references `albums`(`id`) on delete cascade;

-- alter table `albums` add constraint `albums_fk0` foreign key (`actor_id`) references `actors`(`id`) on delete cascade;

-- alter table `albums` add constraint `albums_fk1` foreign key (`studio_id`) references `studios`(`id`) on delete cascade;
