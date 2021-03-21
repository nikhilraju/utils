import argparse
import logging

def parse_args():
    parser = argparse.ArgumentParser(
        description="""A template example for argparse arguments""")
    # Input, Output and Model directories
    parser.add_argument('--input_file', type=str, required=True,
                        help='A spreadsheet with text documents')
    parser.add_argument('--train', action='store_true')
    parser.add_argument('--models_dir', type=str, default='.',
                        help='The directory used to store trained models')
    parser.add_argument('--saved_model_path', type=str,
                        help='The path of a model that has been trained and saved already')
    parser.add_argument('--output_dir', type=str, default='.',
                        help='The directory used to store results')
    parser.add_argument('--visualize_clusters', action='store_true')

    # Model hyperparameters that can be passed as command-line arguments to the script
    parser.add_argument('--embedding_choice', type=str,
                        default='universal-sentence-encoder')
    parser.add_argument('--outlier_score_threshold', type=float, default=0.9)
    parser.add_argument('--outlier_quantile', type=float, default=0.99)
    parser.add_argument('--n_neighbors', type=int, default=25)
    parser.add_argument('--min_cluster_size', type=int, default=50)
    return parser.parse_known_args()

def main():
    logger = logging.getLogger('argparse-arguments-template')
    logger.setLevel(logging.INFO)
    sh = logging.StreamHandler()
    sh.setFormatter(logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(sh)

    logger.info('Parsing arguments...')
    # Discard any additional arguments(not in the parser) without throwing an error
    args, _ = parse_args()
    logger.info('Arguments: %s', args)


if __name__ == '__main__':
	main()
