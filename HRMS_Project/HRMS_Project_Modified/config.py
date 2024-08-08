class Config:
    """
    Use this class to share any default attributes with any subsequent
    classes that inherit from Config.
    """
    DEBUG = False
    TESTING = False
    SECRET_KEY = "otg9vbTH0M"
    SQLALCHEMY_DATABASE_URI = 'mysql://sql6446243:vfIxNcGmv3@sql6.freesqldatabase.com/sql6446243'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECURITY_DEFAULT_HTTP_AUTH_REALM = True


class ProductionConfig(Config):
    """
    This class will inherits any attributes from the parent Config class.
    Use this class to define production configuration atrributes, such
    as database usernames, passwords, server specific files & directories etc.
    Right now no production configuration is done
    """
    pass


class DevelopmentConfig(Config):
    """
    This class will inherits any attributes from the parent Config class.
    Use this class to define development configuration atrributes, such
    as local database usernames, passwords, local specific files & directories etc.
    """
    DEBUG = True