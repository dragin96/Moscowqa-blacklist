-- Создание таблицы blacklist_users
CREATE TABLE IF NOT EXISTS blacklist_users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    phone_numbers TEXT[] NOT NULL,
    emails TEXT[] NOT NULL,
    telegrams TEXT[] NOT NULL,
    comment TEXT NOT NULL
);

-- Вставка тестовых данных
INSERT INTO blacklist_users (id, first_name, last_name, phone_numbers, emails, telegrams, comment)
VALUES
    (
        gen_random_uuid(),
        'John',
        'Doe',
        ARRAY['+123456789', '+987654321'],
        ARRAY['john.doe@example.com', 'j.doe@gmail.com'],
        ARRAY['@johndoe'],
        'Test reason: suspicious activity'
    ),
    (
        gen_random_uuid(),
        'Jane',
        'Smith',
        ARRAY['+1122334455'],
        ARRAY['jane.smith@example.com'],
        ARRAY['@janesmith'],
        'Test reason: spam complaints'
    ),
    (
        gen_random_uuid(),
        'Alice',
        'Johnson',
        ARRAY['+9988776655', '+5566778899'],
        ARRAY['alice.johnson@example.com'],
        ARRAY['@alicejohnson'],
        'Test reason: fraudulent transactions'
    );
