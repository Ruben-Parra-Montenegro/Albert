use clap::Parser;
use std::{fs,path::PathBuf};

#[derive(Debug, Parser)]
#[command(version,about,long_about = "Helpful tool for managing Albert")]
struct CLI{
    path:Option<PathBuf>,
}

fn main() {
    let cli = CLI::parse();

    let path = cli.path.unwrap_or(PathBuf::from("."));

    if let Ok(does_exist) = fs::exists(&path){
        if does_exist{

        }else{
            println!("{}","Path does not exist.");
        }
    }
}
