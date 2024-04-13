const path = require('path');
const HtmlWebpackPlugin = require("html-webpack-plugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");


module.exports = {
    entry: "./src/index.js",
    output: {
        path: path.join(__dirname, "/dist"),
        filename: "bundle.js"
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude:/node_modules/,
                use: {
                    loader: "babel-loader"
                }
            },
            {
                test: /\.css$/,
                use: [
                    {
                    loader: MiniCssExtractPlugin.loader,
                    options: {
                        esModule: true,
                    },
                    },
                    'css-loader',
                ],
            }
        ]
    },
    stats: {
        children: true
    },
    plugins: [
        new HtmlWebpackPlugin({template: './dist/index.html'}),
        new MiniCssExtractPlugin(),
    ]
    }
