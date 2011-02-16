USE kakuro;

DROP TABLE IF EXISTS combos;
DROP TABLE IF EXISTS number_combos;

CREATE TABLE combos (
  id INT NOT NULL AUTO_INCREMENT,
  slots INT NOT NULL,
  sum INT NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE number_combos (
  id INT NOT NULL AUTO_INCREMENT,
  combo_id INT NOT NULL,
  number_value INT NOT NULL,
  PRIMARY KEY (id),
  UNIQUE (combo_id, number_value)
);

