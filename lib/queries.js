module.exports = {
	getNotificationCount : `
		SELECT COUNT(*) nb
		FROM notification
		WHERE title = ?
		AND text = ?`,
	
	deleteAlarm : `
		DELETE
		FROM alarm
		WHERE name = ?`,
	
	deleteScript : `
		DELETE
		FROM script
		WHERE name = ?`,
	
	deleteAction : `
		DELETE
		FROM action
		WHERE launcher = (
			SELECT id
			FROM launcher
			WHERE title = ?
		)`,
	
	deleteLauncher : `
		DELETE
		FROM launcher
		WHERE title = ?`,
	
	deleteAllNotifications : `
		DELETE
		FROM notification
		WHERE link = ?`
};