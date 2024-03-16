CREATE OR REPLACE VIEW appointments_total_payments AS (
    SELECT
        c.full_name,
        a.cabinet,
        cp.total,
        a.start_time,
        a.end_time
    FROM appointments a
        LEFT JOIN client_payments cp ON a.id = cp.appointment_id
        LEFT JOIN clients c ON c.id = a.client_id
);