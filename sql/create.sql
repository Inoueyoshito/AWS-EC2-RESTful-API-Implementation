DROP TABLE IF EXISTS recipes;

CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    making_time VARCHAR(100) NOT NULL,
    serves VARCHAR(100) NOT NULL,
    ingredients TEXT NOT NULL,
    cost INTEGER NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO
    recipes (
        id,
        title,
        making_time,
        serves,
        ingredients,
        cost,
        created_at,
        updated_at
    )
VALUES
    (
        1,
        'チキンカレー',
        '45分',
        '4人',
        '玉ねぎ,肉,スパイス',
        1000,
        '2016-01-10 12:10:12',
        '2016-01-10 12:10:12'
    );

INSERT INTO
    recipes (
        id,
        title,
        making_time,
        serves,
        ingredients,
        cost,
        created_at,
        updated_at
    )
VALUES
    (
        2,
        'オムライス',
        '30分',
        '2人',
        '玉ねぎ,卵,スパイス,醤油',
        700,
        '2016-01-11 13:10:12',
        '2016-01-11 13:10:12'
    );