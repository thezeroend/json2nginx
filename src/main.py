from application.config_service import main
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Processa arquivos de configuração JSON e gera arquivos .conf.")
    parser.add_argument(
        "--configs-dir",
        type=str,
        required=True,
        help="Diretório onde estão os arquivos de configuração JSON."
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="../outputs",
        help="Diretório onde os arquivos .conf serão gerados."
    )

    args = parser.parse_args()
    main(args.configs_dir, args.output_dir)
