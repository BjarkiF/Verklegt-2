let creds = () => {
    return {
        'customer': {
            'username': process.env.REST_CUSTOMER_USERNAME,
            'password': process.env.REST_CUSTOMER_PASSWORD
        },
        'employee': {
            'username': process.env.REST_EMPLOYEE_PASSWORD,
            'password': process.env.REST_EMPLOYEE_PASSWORD
        },
        'staff': {
            'username': process.env.REST_STAFF_USERNAME,
            'password': process.env.REST_STAFF_PASSWORD
        },
        'superuser': {
            'username': process.env.REST_SUPERUSER_USERNAME,
            'password': process.env.REST_SUPERUSER_PASSWORD
        }
    }
}

exports.creds = creds
