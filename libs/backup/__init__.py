"""
Requires awscli
Setup credentials in user on servers.

BACKUP_ENABLED = True

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket",
                "s3:GetObjectAttributes"
            ],
            "Resource": "arn:aws:s3:::leasyfi-erpnext-backup"
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:PutObjectAcl"
            ],
            "Resource": [
                "arn:aws:s3:::leasyfi-erpnext-backup/*"
            ]
        }
    ]
}

"""
