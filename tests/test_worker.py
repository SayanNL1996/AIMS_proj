import unittest
import mock
from users.worker import Worker
from database_connection import DatabaseConnection
from query import Queries


class workerTest(unittest.TestCase):

    def setUp(self):
        self.worker = Worker()

    @mock.patch.object(Worker, 'show_worker_profile')
    @mock.patch.object(Worker, 'show_active_complaints')
    @mock.patch.object(Worker, 'show_complaint_history')
    @mock.patch.object(Worker, 'create_complaint')
    @mock.patch('builtins.input')
    def test_worker_tasks(self, mock_input, mock_create_complaint, mock_show_complaint_history,
                          mock_show_active_complaints, mock_show_worker_profile):
        # choice = 1
        mock_input.return_value = 1
        self.worker.worker_tasks()
        mock_create_complaint.assert_called_once()

        # choice = 2
        mock_input.return_value = 2
        self.worker.worker_tasks()
        mock_show_complaint_history.assert_called_once()

        # choice = 3
        mock_input.return_value = 3
        self.worker.worker_tasks()
        mock_show_active_complaints.assert_called_once()

        # choice = 4
        mock_input.return_value = 4
        self.worker.worker_tasks()
        mock_show_worker_profile.assert_called_once()

        # choice = 5
        mock_input.return_value = 4
        self.worker.worker_tasks()
        self.assertRaises(Exception, 4)

    @mock.patch.object(Worker, 'input_create_complaint_data')
    @mock.patch('builtins.print')
    def test_create_complaint(self, mock_input, mock_input_create_complaint_data):
        b = ('fire breakout', 'xyz', '1')
        mock_input_create_complaint_data.return_value = b
        self.instance_Worker.create_complaint()

    @mock.patch.object(Worker, "worker_tasks")
    @mock.patch.object(DatabaseConnection, "dbconnection")
    @mock.patch('builtins.input')
    def test_create_complaint(self, mock_input, mock_dbconnection, mock_worker_tasks):
        mock_conn = mock.Mock()
        mock_cursor = mock.Mock()
        mock_dbconnection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        mock_input.side_effect = ('fire breakout', 'abc')
        query = Queries.create.value
        mock_cursor.execute.assert_called_once_with(query.format('fire breakout', 'abc'))
        mock_worker_tasks.assert_called_once()

    @mock.patch.object(DatabaseConnection, "dbconnection")
    @mock.patch('builtins.input')
    def test_show_complaint_history(self, mock_input, mock_dbconnection):
        mock_conn = mock.Mock()
        mock_cursor = mock.Mock()
        mock_dbconnection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        data = [('1', 'xyz', 'abc')]
        mock_cursor.execute.return_value = data
        mock_input.return_value = 1
        mock_input.assert_called_once()
        self.worker.show_complaint_history()

    @mock.patch.object(DatabaseConnection, "dbconnection")
    @mock.patch('builtins.input')
    def test_show_active_complaints(self, mock_input, mock_dbconnection):
        mock_conn = mock.Mock()
        mock_cursor = mock.Mock()
        mock_dbconnection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        data = [('1', 'xyz', 'abc')]
        mock_cursor.execute.return_value = data
        mock_input.return_value = 1
        mock_input.assert_called_once()
        self.worker.show_active_complaints()

    @mock.patch.object(DatabaseConnection, "dbconnection")
    @mock.patch('builtins.input')
    def test_show_worker_profile(self, mock_input, mock_dbconnection):
        mock_conn = mock.Mock()
        mock_cursor = mock.Mock()
        mock_dbconnection.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor
        data = [('1', 'xyz', 'abc')]
        mock_cursor.execute.return_value = data
        mock_input.return_value = 1
        mock_input.assert_called_once()
        self.worker.show_worker_profile()


if __name__ == '__main__':
    unittest.main()
