
"""Manage bike-share stations, bike rentals, and unlock PINs."""

import secrets
import sqlite3


def create_database():
    """Create an in-memory database for bike-share stations."""
    connection = sqlite3.connect(":memory:")
    connection.execute(
        "CREATE TABLE stations ("
        "id INTEGER PRIMARY KEY, "
        "name TEXT, "
        "capacity INTEGER, "
        "bikes INTEGER)"
    )
    return connection


def add_station(connection, name, capacity, bikes, log=None):
    """Add a bike station and record its name in the log."""
    if not name or capacity < 0 or bikes < 0 or bikes > capacity:
        raise ValueError("Invalid station details")

    if log is None:
        log = []

    connection.execute(
        "INSERT INTO stations (name, capacity, bikes) "
        "VALUES (?, ?, ?)",
        (name, capacity, bikes)
    )
    log.append(name)
    return log


def rent_bike(connection, station_id):
    """Rent a bike if the station has bikes available."""
    row = connection.execute(
        "SELECT bikes FROM stations WHERE id = ?",
        (station_id,)
    ).fetchone()

    if row is not None and row[0] > 0:
        connection.execute(
            "UPDATE stations SET bikes = bikes - 1 WHERE id = ?",
            (station_id,)
        )
        return True

    return False


def unlock_pin():
    """Generate a secure four-digit unlock PIN."""
    return secrets.randbelow(9000) + 1000


def full_stations(connection):
    """Return the names of stations that are at full capacity."""
    stations = connection.execute(
        "SELECT name FROM stations WHERE bikes = capacity"
    ).fetchall()

    return [station[0] for station in stations]


def reset_station(connection, station_id):
    """Reset the bike count of a station to zero."""
    try:
        cursor = connection.execute(
            "UPDATE stations SET bikes = 0 WHERE id = ?",
            (station_id,)
        )
        return cursor.rowcount > 0
    except sqlite3.Error as error:
        print(f"Database error while resetting station: {error}")
        return False


def has_bikes(connection, station_id):
    """Check whether a station has available bikes."""
    row = connection.execute(
        "SELECT bikes FROM stations WHERE id = ?",
        (station_id,)
    ).fetchone()

    if row is None or row[0] is None:
        return False

    return row[0] > 0


def main():
    """Demonstrate the bike-share station operations."""
    connection = create_database()

    try:
        add_station(connection, "Central Park", 10, 10)
        add_station(connection, "Metro Gate", 8, 2)

        print(rent_bike(connection, 2),
              not rent_bike(connection, 9))
        print(unlock_pin(), full_stations(connection),
              has_bikes(connection, 2))
        reset_station(connection, 1)
    finally:
        connection.close()


if __name__ == "__main__":
    main()
