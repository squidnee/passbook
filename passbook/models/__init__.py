import enum
import json

from datetime import datetime
from passbook.features.orm import db

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

PERSONAL_NOTE_FIELDS = {
	"Name": {
		"First Name": "",
		"Middle Name": "",
		"Last Name": "",
		"Date of Birth": ""
	},
	"Email": {
		"Email Address": "",
		"Type": ["Personal", "Work", "School", "Other"]
	},
	"Mobile": {
		"Phone Number": "",
		"Type": ["Cell", "Home", "Work"]
	},
	"Details": {
		"Address": {
			"Address": "",
			"City": "",
			"State": "",
			"Zip Code": "",
			"Country": ""
		},
		"Company": {
			"Company Name": "",
			"Job Title": ""
		},
		"Website": {
			"Website URL": ""
		},
		"Messenger": {
			"Service": "",
			"Username": ""
		}
	}
}

IDENTIFICATION_NOTE_FIELDS = {
	"Social Security": {
		"Card Number": "",
		"Full Name": "",
		"Gender": ["Male", "Female"],
		"Date of Birth": "",
	},
	"Passport": {
		"Issued Location": "",
		"Issued Date": "",
		"Expiration Date": ""
	},
	"Drivers License": {
		"State Issued": "",
		"Issue Date": "",
		"Expiration Date": ""
	},
	"Birth Certificate": {
		"Document Name": "",
		"Document Type": "",
		"Document Number": "",
		"Issuing Country": "",
		"Full Name": "",
		"Nationality": "",
		"Issuing Authority": "",
		"Place of Birth": "",
		"Date of Birth": "",
		"Issued Location": "",
		"Issued Date": "",
		"Expiration Date": ""
	},
	"Insurance Card": {
		"Insurance Type": "",
		"ID Number": "",
		"Group Number": ""
	}
}

WALLET_NOTE_FIELDS = {
	"Credit Card": {
		"Cardholder Name": "",
		"Card Number": "",
		"Security Code": "",
		"Expiration Date": "",
		"Billing Address": {
			"Address": "",
			"City": "",
			"State": "",
			"Zip Code": "",
			"Country": ""
		},
		"Card Type": ["Credit", "Debit"],
		"Bank Name": ""
	},
	"Bank Account": {
		"Account Holder": "",
		"Routing Number": "",
		"Account Number": "",
		"Bank Name": "",
		"PIN": "",
		"Bank Phone Number": "",
		"Bank Address": ""
	},
	"Membership": {
		"Service or Company Name": "",
		"Membership ID": "",
		"Card Number": "",
		"Email": ""
	},
	"Receipt": {
		"Currency": "",
		"Price": "",
		"Date": "",
		"Store/Service Name": ""
	}
}

COMPUTER_NOTE_FIELDS = {
	"Wifi": {
		"Network Name": "",
		"Network Password": "",
		"Server/IP Address": "",
		"Support Phone Number": ""
	},
	"Server": {
		"URL": "",
		"Hostname": "",
		"Username": "",
		"Password": "",
		"Admin Username": "",
		"Admin Password": "",
		"Support Phone Number": ""
	},
	"Database": {
		"Name": "",
		"Server": "",
		"Port": "",
		"Username": "",
		"Password": "",
		"SID": ""
	},
	"Software License": {
		"Version": "",
		"Licensed To": "",
		"License Key": "",
		"Registered Email": "",
		"Distributor Name": "",
		"Distributor Website": ""
	},
	"SSH Keys": {
		"Hostname": "",
		"Passphrase": "",
		"Private Key": "",
		"Public Key": ""
	}
}

NOTE_FIELDS = {
	"Personal Information": json.dumps(PERSONAL_NOTE_FIELDS),
	"Identification": json.dumps(IDENTIFICATION_NOTE_FIELDS),
	"Wallet": json.dumps(WALLET_NOTE_FIELDS),
	"Computer": json.dumps(COMPUTER_NOTE_FIELDS)
}

class ColorType(enum.Enum):
	Red = 1
	Orange = 2
	Yellow = 3
	Green = 4
	Blue = 5
	Purple = 6