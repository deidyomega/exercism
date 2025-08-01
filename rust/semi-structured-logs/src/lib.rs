// This stub file contains items which aren't used yet; feel free to remove this module attribute
// to enable stricter warnings.

/// various log levels
#[derive(Clone, PartialEq, Debug)]
pub enum LogLevel {
    Info,
    Warning,
    Error,
    Debug,
}

fn capitalize_log_level(level: LogLevel) -> String {
    match level {
        LogLevel::Info => "INFO".to_string(),
        LogLevel::Warning => "WARNING".to_string(),
        LogLevel::Error => "ERROR".to_string(),
        LogLevel::Debug => "DEBUG".to_string(),
    }
}

/// primary function for emitting logs
pub fn log(level: LogLevel, message: &str) -> String {
    format!("[{}]: {}", capitalize_log_level(level), message)
}
pub fn info(message: &str) -> String {
    log(LogLevel::Info, message)
}
pub fn warn(message: &str) -> String {
    log(LogLevel::Warning, message)
}
pub fn error(message: &str) -> String {
    log(LogLevel::Error, message)
}
pub fn debug(message: &str) -> String {
    log(LogLevel::Debug, message)
}
