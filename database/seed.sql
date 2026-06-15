INSERT INTO environments (name, description)
VALUES (
        'Development',
        'Development Environment'
    ),
    (
        'QA',
        'Quality Assurance Environment'
    ),
    (
        'Production',
        'Production Environment'
    );
INSERT INTO servers (
        environment_id,
        hostname,
        ip_address,
        operating_system,
        status
    )
VALUES (
        1,
        'dev-api-01',
        '10.0.1.10',
        'Ubuntu 24.04',
        'ACTIVE'
    ),
    (
        2,
        'qa-api-01',
        '10.0.2.10',
        'Ubuntu 24.04',
        'ACTIVE'
    ),
    (
        3,
        'prod-api-01',
        '10.0.3.10',
        'Ubuntu 24.04',
        'ACTIVE'
    ),
    (
        3,
        'prod-db-01',
        '10.0.3.20',
        'PostgreSQL Linux',
        'ACTIVE'
    );
INSERT INTO applications (
        server_id,
        name,
        version,
        status
    )
VALUES (
        1,
        'CloudOps API',
        '1.0.0',
        'RUNNING'
    ),
    (
        2,
        'CloudOps API',
        '1.0.0',
        'RUNNING'
    ),
    (
        3,
        'CloudOps API',
        '1.0.0',
        'RUNNING'
    ),
    (
        4,
        'PostgreSQL',
        '17.10',
        'RUNNING'
    );