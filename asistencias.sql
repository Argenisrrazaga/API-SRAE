CREATE TABLE IF NOT EXISTS `Estudiante` (
	`id` integer primary key NOT NULL UNIQUE,
	`nombre` TEXT NOT NULL,
	`apellido` INTEGER NOT NULL
);
CREATE TABLE IF NOT EXISTS `Curso` (
	`id` integer primary key NOT NULL UNIQUE,
	`nombre` TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS `Asistencia` (
	`id` integer primary key NOT NULL UNIQUE,
	`fecha` REAL NOT NULL,
	`estudiante_id` INTEGER NOT NULL,
	`curso_id` INTEGER NOT NULL,
	`asistio` INTEGER NOT NULL,
FOREIGN KEY(`estudiante_id`) REFERENCES `Estudiante`(`id`),
FOREIGN KEY(`curso_id`) REFERENCES `Curso`(`id`)
);


FOREIGN KEY(`estudiante_id`) REFERENCES `Estudiante`(`id`)
FOREIGN KEY(`curso_id`) REFERENCES `Curso`(`id`)